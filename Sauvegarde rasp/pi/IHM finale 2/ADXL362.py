############################################################
### Library for Communicating with ADXL362 Accelerometer ###
### for Raspberry Pi using spidev                        ###
###                                                      ###
### Authors: Sam Zeckendorf                              ###
###          Nathan Tarrh                                ###
###    Date: 3/29/2014                                   ###
############################################################

# spidev is the Raspberry Pi spi communication library
import spidev
import time

class ADXL362:

    def __init__(self, device=0, ce_pin=0):
        """
        device: the SPI device (often 0)

        ce_pin: pass 0 for CE0, 1 for CE1, etc.

        device and ce_pin map to device file /dev/spidev{device}.{ce_pin}
        """

        # init spi for communication
        self.spi = spidev.SpiDev()      #Creation d'un objet spi
        self.spi.open(device, ce_pin)   # (x,0) == CE0, (x,1) == CE1

        # Set clock phase and polarity to default
        self.spi.mode = 0b00        #Polarite et phase de l'horloge a zero
        time.sleep(.5)
      
        self.spi_write_reg(0x1F, 0x52)  #Soft reset
        time.sleep(.01)

        print('Soft reset 1')
    
    def spi_write_reg(self, address, value):
        ''' Write value to address
            Arguments:
                - address: Hexidecimal value of register address
                -   value: Desired hexidecimal byte to write
        '''
        # Send instruction (write), address, and value
        self.spi.xfer2([0x0A, address, value])
        
    def spi_read_reg(self, address):
        ''' Read contents of register at specified address
            Arguments:
                - address: Hexidecimal value of register address
            Returns:
                - value at address
        '''

        # Send instruction (read)
        response = self.spi.xfer2([0x0B, address, 0x00])
        return response[-1]

    def begin_measure(self):
        ''' Turn on measurement mode, required after reset
        '''
        self.spi.cshigh = False     #Chip Select deactivated
        
        # Read in current value in power control register
        pc_reg = self.spi_read_reg(0x2D)
        print(pc_reg)
        
        # Mask measurement mode onto power control buffer
        ##Description : superposition en binaire, lance la mesure des 
        ##accelerations tout en gardant les parametres precedents de 0x2D
        ###Exemple : 1001|1010=1011 soit 9|10=11, ou 45|48=61
        pc_reg_new = pc_reg | 0x02

        # Write new power control buffer to register
        self.spi_write_reg(0x2D, pc_reg_new)

        print(pc_reg_new)

        response = self.spi.xfer2([0x0B, 0x2D, 0x00])
        print(response)
        self.spi.cshigh = True      #CS activated
        time.sleep(.01)

    def read_x(self):
        ''' Read the x value
            Returns:
                - Value of ug in x direction
        '''
        x = self.spi_read_two(0x0E)     #lecture des deux octets consecutifs
        return x

    def read_y(self):
        ''' Read the y value
            Returns:
                - Value of ug in the y direction
        '''
        y = self.spi_read_two(0x10)
        return y

    def read_z(self):
        ''' Read the z value
            Returns:
                - Value of ug in the z direction
        '''
        z = self.spi_read_two(0x12)
        return z

    def read_temp(self):
        ''' Read the temperature value (for calibration/correlation)
            Returns:
                - Internal device temperature
        '''
        temp = self.spi_read_two(0x14)
        return temp

    def read_xyz(self):
        ''' Read x, y, and z data in burst mode. A burst read is required to
            guarantee all measurements correspond to the same sample time.
            Returns:
                - Tuple with x, y, z, and temperature data
        '''
        self.spi.cshigh = False     #Permet d'avoir les donnees au mm moment
        x = self.read_x()
        y = self.read_y()
        z = self.read_z()
        temp = self.read_temp()

        self.spi.cshigh = True
        return (x, y, z, temp)
        
    def spi_read_two(self, address):
        ''' Read two sequential registers : one axis is coded on 16bits
            Arguments: 
                - address: Hexidecimal address of first register to read from
            Returns: 
                - Value contained within said two registers
        '''
       
        # Send read instruction
        ##Faire attention, le premier argument est ici 0x0B, pour la lecture,  
        ##et non 0x0A pour les écritures
        ##Valeur lue en decimal
        value = self.spi.xfer2([0x0B, address, 0x00, 0x00])		
      
        # Isolate low and high bytes from response
        val_l = value[2]
        val_h = value[3] << 8   #Multiplie par 2**8 : bit de poids fort
        
        # Append low byte and high byte together
        value = (val_l + val_h) 

        # Turn format of response into hexidecimal for parsing
        ##Plusieurs etapes :
        ##  a)Codage de value en hexa sous forme '0xaa' en 6 termes mini ici
        ##  b)Conversion en entier
        ##  c)Envoi a two_comp pour le signe : complement a 2
        ###Utilite : independant de type(value), fonctionne en base 2,10,16,...
        return self.twos_comp(int("{0:#0{1}x}".format(value,6), 16), 16)
       
    def spi_write_two(self, address, value):
        ''' Write to two sequential registers
            Arguments: 
                - address: Hexidecimal address of first register to write from
                -   value: Value to be written
        '''
        # Split value into high and low bytes for writing
        high_byte = value >> 8      #Conserve les bits > 8eme
        low_byte = value & 0xFF     #Conserve les 8bits de poids faible
       
        # Send write instruction
        self.spi.xfer2([0x0A, address, low_byte, high_byte])
       
        return value
    
    def check_all_regs(self):
        '''Lit l'ensemble des donnees a partir de 0x20 jusqu'a 0x2E
        '''
        instructions = [0x0B, 0x20]
        registers = [0x00] * 15
        instructions.extend(registers)
        values = self.spi.xfer2(instructions)
        
        return values[2:]

    def twos_comp(self,val, bits):
        """ Returns two's complement of value given a number of bits
        """
        #Complement a 2: on enleve 2**x si c'est négatif, ainsi on a des
        #donnees entre (1 - 2**x) et (2**x - 1)
        if val&(1<<(bits-1)) != 0:      #Si bit négatif actif
            val = val - (1<<bits)       
        return val

