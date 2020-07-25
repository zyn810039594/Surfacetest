import binascii
class Analyse():
    def BaseIn(self, datahex: bytes):
        state = 0
        Acceleration = (0.0, 0.0, 0.0)
        Palstance = (0.0, 0.0, 0.0)
        Euler_angle = (0.0, 0.0, 0.0)
        danger = 0
        Power = 0.0
        if len(datahex) > 26 and datahex[-1] == 255 and datahex[-27] == 255 and datahex[-26]==238:
            def3 = datahex[-27]
            for data in datahex[-26:-2]:
                def3 ^= data
            if def3 == datahex[-2]:
                state = 1
                danger = datahex[-3]
            else:
                state = 2
            test=datahex[-27:-1]
            Acceleration = self.get_acc(datahex[-25:-19])
            Palstance = self.get_gyro(datahex[-19:-13])
            Euler_angle = self.get_angle(datahex[-13:-7])
            Power = datahex[-4] / 10

        return state, Power, danger, Acceleration, Palstance, Euler_angle

    def get_acc(self, datahex: bytes):
        axl = datahex[0]
        axh = datahex[1]
        ayl = datahex[2]
        ayh = datahex[3]
        azl = datahex[4]
        azh = datahex[5]

        k_acc = 16.0

        acc_x = (axh << 8 | axl) / 32768.0 * k_acc
        acc_y = (ayh << 8 | ayl) / 32768.0 * k_acc
        acc_z = (azh << 8 | azl) / 32768.0 * k_acc
        if acc_x >= k_acc:
            acc_x -= 2 * k_acc
        if acc_y >= k_acc:
            acc_y -= 2 * k_acc
        if acc_z >= k_acc:
            acc_z -= 2 * k_acc

        return acc_x, acc_y, acc_z

    def get_gyro(self, datahex: bytes):
        wxl = datahex[0]
        wxh = datahex[1]
        wyl = datahex[2]
        wyh = datahex[3]
        wzl = datahex[4]
        wzh = datahex[5]
        k_gyro = 2000.0

        gyro_x = (wxh << 8 | wxl) / 32768.0 * k_gyro
        gyro_y = (wyh << 8 | wyl) / 32768.0 * k_gyro
        gyro_z = (wzh << 8 | wzl) / 32768.0 * k_gyro
        if gyro_x >= k_gyro:
            gyro_x -= 2 * k_gyro
        if gyro_y >= k_gyro:
            gyro_y -= 2 * k_gyro
        if gyro_z >= k_gyro:
            gyro_z -= 2 * k_gyro
        return gyro_x, gyro_y, gyro_z

    def get_angle(self, datahex: bytes):
        rxl = datahex[0]
        rxh = datahex[1]
        ryl = datahex[2]
        ryh = datahex[3]
        rzl = datahex[4]
        rzh = datahex[5]
        k_angle = 180.0

        angle_x = (rxh << 8 | rxl) / 32768.0 * k_angle
        angle_y = (ryh << 8 | ryl) / 32768.0 * k_angle
        angle_z = (rzh << 8 | rzl) / 32768.0 * k_angle
        if angle_x >= k_angle:
            angle_x -= 2 * k_angle
        if angle_y >= k_angle:
            angle_y -= 2 * k_angle
        if angle_z >= k_angle:
            angle_z -= 2 * k_angle

        return angle_x, angle_y, angle_z

    def BaseOut(self, straight,side, A1V, A2V, A3V):
        SendByteStr = bytearray(b"\xff\xee\x00\x00\x00\x00\x00\x00\x00\x00\x00\xef\xfe")
        BackText=None
        AF=straight>side
        BF=(straight+side)>256
        CF=straight>128
        DF=side>128
        SF=AF*8+BF*4+CF*2+DF
        if (SF==0) or (SF==15):
            SendByteStr[2]=side
            SendByteStr[4]=128-side+straight
        elif (SF==7) or (SF==8):
            SendByteStr[2] = straight
            SendByteStr[4] = 128 - side + straight
        elif (SF==5) or (SF==10):
            SendByteStr[2]=straight+side-128
            SendByteStr[4]=straight
        elif (SF==1) or (SF==14):
            SendByteStr[2] = straight + side - 128
            SendByteStr[4] = 256-side

        SendByteStr[6]=A1V
        SendByteStr[7]=A2V
        SendByteStr[8]=A3V
        def3,def4,def5=self.cac_send_def(SendByteStr)
        SendByteStr[3]=def3
        SendByteStr[5]=def4
        SendByteStr[10]=def5
        Send_Bytes=bytes(SendByteStr)
        SendByteStr = bytes(SendByteStr)
        Send_Str = binascii.hexlify(SendByteStr)
        Send_Str = Send_Str.decode()
        return BackText,Send_Bytes,Send_Str


    def cac_send_def(self, datahex: bytes):
        mot1 = datahex[2]
        mot2 = datahex[4]
        th1 = datahex[6]
        th3 = datahex[8]
        th4 = datahex[9]
        def6 = datahex[11]
        def4 = abs((th1 - def6) >> 18) * 3
        def3 = int((abs(mot1 - mot2 + th3 - th4) << 8) / abs(def4<<8 + 1))
        def5 = datahex[0]
        for byte in datahex[1:9]:
            def5 ^= byte
        return def3, def4, def5
