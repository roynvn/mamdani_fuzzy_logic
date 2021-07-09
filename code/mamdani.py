from time import time

#KESADAHAN
kesadahanLunakmin = 0
kesadahanLunakmax = 50

kesadahanMediummin = 45
kesadahanMediummax = 150

kesadahanKerasmin = 145
kesadahanKerasmax = 500

#Kekeruhan
kekeruhanBersihmin = 0
kekeruhanBersihmax = 10

kekeruhanCukupBersihmin = 5
kekeruhanCukupBersihmax = 25

kekeruhanKeruhmin = 20
kekeruhanKeruhmax = 70

#TDS
TDSBaikmin = 300
TDSBaikmax = 900

TDSBurukmin = 500
TDSBurukmax = 1200

TDSSangatBurukmin = 1150
TDSSangatBurukmax = 2000



def inRange(minimal,maximal,input):
    minimal = min(minimal, maximal)
    maximal = max(minimal, maximal)

    if((input> minimal) and (input < maximal)):
        return 1
    else:
        return 0

def fuzzyRules(kesadahan,kekeruhan,tds):
    global nilaikelayakanrendah
    global nilaikelayakantinggi

    nilaikelayakanrendah = 0
    nilaikelayakantinggi = 0


    #KESADAHAN
    kesadahanLunak = inRange(kesadahanLunakmin,kesadahanLunakmax,kesadahan)
    kesadahanMedium = inRange(kesadahanMediummin,kesadahanMediummax,kesadahan) 
    kesadahanKeras = inRange(kesadahanKerasmin,kesadahanKerasmax,kesadahan)

    #KEKERUHAN
    kekeruhanBersih         = inRange(kekeruhanBersihmin,kekeruhanBersihmax,kekeruhan)
    kekeruhanCukupBersih    = inRange(kekeruhanCukupBersihmin,kekeruhanCukupBersihmax,kekeruhan)
    kekeruhanKeruh          = inRange(kekeruhanKeruhmin,kekeruhanKeruhmax,kekeruhan)

    #TDS
    TDSBaik        = inRange(TDSBaikmin,TDSBaikmax,tds)
    TDSBuruk       = inRange(TDSBurukmin,TDSBurukmax,tds)
    TDSSangatBuruk = inRange(TDSSangatBurukmin,TDSSangatBurukmax,tds)

    nkrendah_array = []
    nktinggi_array = []

    if kesadahanLunak == 1 and kekeruhanBersih == 1 and TDSBaik == 1:
        print("Rule 1: Kesadahan: Lunak dan Kekeruhan: Bersih dan TDS:Baik")
        derajatkelayakantinggi = min(derajatkesadahanlunak,derajatkekeruhanbersih,derajattdsbaik)
        print("Derajat Kelayakan Tinggi",derajatkelayakantinggi)
        nilaikelayakantinggi = derajatkelayakantinggi
        nktinggi = nktinggi_array.append(nilaikelayakantinggi)

    if kesadahanLunak == 1 and kekeruhanBersih == 1 and TDSBuruk == 1:
        print("Rule 2: Kesadahan: Lunak dan Kekeruhan: Bersih dan TDS:Buruk")
        derajatkelayakantinggi = min(derajatkesadahanlunak,derajatkekeruhanbersih,derajattdsburuk)
        print("Derajat Kelayakan Tinggi",derajatkelayakantinggi)
        nilaikelayakantinggi = derajatkelayakantinggi
        nktinggi = nktinggi_array.append(nilaikelayakantinggi)

    if kesadahanLunak == 1 and kekeruhanBersih == 1 and TDSSangatBurukmin == 1:
        print("Rule 3: Kesadahan: Lunak dan Kekeruhan: Bersih dan TDS:Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahanlunak,derajatkekeruhanbersih,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanLunak == 1 and kekeruhanCukupBersih == 1 and TDSBaik == 1:
        print("Rule 4: Kesadahan: Lunak dan Kekeruhan: Cukup Bersih dan TDS:Baik")
        derajatkelayakantinggi = min(derajatkesadahanlunak,derajatkekeruhancukupbersih,derajattdsbaik)
        print("Derajat Kelayakan Tinggi",derajatkelayakantinggi)
        nilaikelayakantinggi = derajatkelayakantinggi
        nktinggi = nktinggi_array.append(nilaikelayakantinggi)

    if kesadahanLunak == 1 and kekeruhanCukupBersih == 1 and TDSBuruk == 1:
        print("Rule 5: Kesadahan: Lunak dan Kekeruhan: Cukup Bersih dan TDS:Buruk")
        derajatkelayakanrendah = min(derajatkesadahanlunak,derajatkekeruhancukupbersih,derajattdsburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)
    
    if kesadahanLunak == 1 and kekeruhanCukupBersih == 1 and TDSSangatBuruk == 1:
        print("Rule 6: Kesadahan: Lunak dan Kekeruhan: Cukup Bersih dan TDS: Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahanlunak,derajatkekeruhancukupbersih,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)
    
    if kesadahanLunak == 1 and kekeruhanKeruh == 1 and TDSBaik == 1:
        print("Rule 7: Kesadahan: Lunak dan Kekeruhan: Keruh dan TDS:Baik")
        derajatkelayakanrendah = min(derajatkesadahanlunak,derajatkekeruhankeruh,derajattdsbaik)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanLunak == 1 and kekeruhanKeruh == 1 and TDSBuruk == 1:
        print("Rule 8: Kesadahan: Lunak dan Kekeruhan: Keruh dan TDS:Buruk")
        derajatkelayakanrendah = min(derajatkesadahanlunak,derajatkekeruhankeruh,derajattdsburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanLunak == 1 and kekeruhanKeruh == 1 and TDSSangatBuruk == 1:
        print("Rule 9: Kesadahan: Lunak dan Kekeruhan: Keruh dan TDS:Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahanlunak,derajatkekeruhankeruh,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanMedium  == 1 and kekeruhanBersih == 1 and TDSBaik == 1:
        print("Rule 10: Kesadahan: Medium dan Kekeruhan: Bersih dan TDS:Baik")
        derajatkelayakantinggi = min(derajatkesadahanmedium,derajatkekeruhanbersih,derajattdsbaik)
        print("Derajat Kelayakan Tinggi",derajatkelayakantinggi)
        nilaikelayakantinggi = derajatkelayakantinggi
        nktinggi = nktinggi_array.append(nilaikelayakantinggi)

    if kesadahanMedium  == 1 and kekeruhanBersih == 1 and TDSBuruk == 1:
        print("Rule 11: Kesadahan: Medium dan Kekeruhan: Bersih dan TDS:Buruk")
        derajatkelayakanrendah= min(derajatkesadahanmedium,derajatkekeruhanbersih,derajattdsburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanMedium == 1 and kekeruhanBersih == 1 and TDSSangatBurukmin == 1:
        print("Rule 12: Kesadahan: Medium dan Kekeruhan: Bersih dan TDS:Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahanmedium,derajatkekeruhanbersih,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanMedium  == 1 and kekeruhanCukupBersih == 1 and TDSBaik == 1:
        print("Rule 13: Kesadahan: Medium dan Kekeruhan: Cukup Bersih dan TDS:Baik")
        derajatkelayakantinggi = min(derajatkesadahanmedium,derajatkekeruhancukupbersih,derajattdsbaik)
        print("Derajat Kelayakan Tinggi",derajatkelayakantinggi)
        nilaikelayakantinggi = derajatkelayakantinggi
        nktinggi = nktinggi_array.append(nilaikelayakantinggi)

    if kesadahanMedium  == 1 and kekeruhanCukupBersih == 1 and TDSBuruk == 1:
        print("Rule 14: Kesadahan: Medium dan Kekeruhan: Cukup Bersih dan TDS:Buruk")
        derajatkelayakanrendah = min(derajatkesadahanmedium,derajatkekeruhancukupbersih,derajattdsburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)
    
    if kesadahanMedium  == 1 and kekeruhanCukupBersih == 1 and TDSSangatBuruk == 1:
        print("Rule 15: Kesadahan: Medium dan Kekeruhan: Cukup Bersih dan TDS: Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahanmedium,derajatkekeruhancukupbersih,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)
    
    if kesadahanMedium  == 1 and kekeruhanKeruh == 1 and TDSBaik == 1:
        print("Rule 16: Kesadahan: Medium dan Kekeruhan: Keruh dan TDS:Baik")
        derajatkelayakanrendah = min(derajatkesadahanmedium,derajatkekeruhankeruh,derajattdsbaik)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanMedium  == 1 and kekeruhanKeruh == 1 and TDSBuruk == 1:
        print("Rule 17: Kesadahan: Medium dan Kekeruhan: Keruh dan TDS:Buruk")
        derajatkelayakanrendah = min(derajatkesadahanmedium,derajatkekeruhankeruh,derajattdsburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanMedium  == 1 and kekeruhanKeruh == 1 and TDSSangatBuruk == 1:
        print("Rule 18: Kesadahan: Medium dan Kekeruhan: Keruh dan TDS:Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahanmedium,derajatkekeruhankeruh,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanKeras == 1 and kekeruhanBersih == 1 and TDSBaik == 1:
        print("Rule 19: Kesadahan: Keras dan Kekeruhan: Bersih dan TDS:Baik")
        derajatkelayakanrendah = min(derajatkesadahankeras,derajatkekeruhanbersih,derajattdsbaik)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanKeras   == 1 and kekeruhanBersih == 1 and TDSBuruk == 1:
        print("Rule 20: Kesadahan: Keras dan Kekeruhan: Bersih dan TDS:Buruk")
        derajatkelayakanrendah= min(derajatkesadahankeras,derajatkekeruhanbersih,derajattdsburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanKeras  == 1 and kekeruhanBersih == 1 and TDSSangatBurukmin == 1:
        print("Rule 21: Kesadahan: Keras dan Kekeruhan: Bersih dan TDS:Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahankeras,derajatkekeruhanbersih,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanKeras   == 1 and kekeruhanCukupBersih == 1 and TDSBaik == 1:
        print("Rule 22: Kesadahan: Keras dan Kekeruhan: Cukup Bersih dan TDS:Baik")
        derajatkelayakanrendah = min(derajatkesadahankeras,derajatkekeruhancukupbersih,derajattdsbaik)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanKeras   == 1 and kekeruhanCukupBersih == 1 and TDSBuruk == 1:
        print("Rule 23: Kesadahan: Keras dan Kekeruhan: Cukup Bersih dan TDS:Buruk")
        derajatkelayakanrendah = min(derajatkesadahankeras,derajatkekeruhancukupbersih,derajattdsburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)
    
    if kesadahanKeras   == 1 and kekeruhanCukupBersih == 1 and TDSSangatBuruk == 1:
        print("Rule 24: Kesadahan: Keras dan Kekeruhan: Cukup Bersih dan TDS: Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahankeras,derajatkekeruhancukupbersih,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)
    
    if kesadahanKeras   == 1 and kekeruhanKeruh == 1 and TDSBaik == 1:
        print("Rule 25: Kesadahan: Keras dan Kekeruhan: Keruh dan TDS:Baik")
        derajatkelayakanrendah = min(derajatkesadahankeras,derajatkekeruhankeruh,derajattdsbaik)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanKeras   == 1 and kekeruhanKeruh == 1 and TDSBuruk == 1:
        print("Rule 26: Kesadahan: Keras dan Kekeruhan: Keruh dan TDS:Buruk")
        derajatkelayakanrendah = min(derajatkesadahankeras,derajatkekeruhankeruh,derajattdsburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if kesadahanKeras   == 1 and kekeruhanKeruh == 1 and TDSSangatBuruk == 1:
        print("Rule 27: Kesadahan: Keras dan Kekeruhan: Keruh dan TDS:Sangat Buruk")
        derajatkelayakanrendah = min(derajatkesadahankeras,derajatkekeruhankeruh,derajattdssangatburuk)
        print("Derajat Kelayakan Rendah",derajatkelayakanrendah)
        nilaikelayakanrendah = derajatkelayakanrendah
        nkrendah = nkrendah_array.append(nilaikelayakanrendah)

    if nilaikelayakantinggi == 0:
        nilaikelayakantinggi = 0
    else:
        nilaikelayakantinggi = max(nktinggi_array)

    if nilaikelayakanrendah == 0:
        nilaikelayakanrendah = 0
    else:
        nilaikelayakanrendah = max(nkrendah_array)

    print("Nilai Kelayakan Rendah : ",nilaikelayakanrendah)
    print("Nilai Kelayakan Tinggi : ",nilaikelayakantinggi)

def centroidMethod(nilaikelayakanrendah, nilaikelayakantinggi):

    global hasil
    hasil =  (((10+20+30+40+50+60)*nilaikelayakanrendah)+((70+80+90+100)*nilaikelayakantinggi))/((6*nilaikelayakanrendah)+(4*nilaikelayakantinggi))
    print("Nilai Kelayakan : ",hasil)
    return hasil


def fungsiKeanggotaanTrapesium(a,b,c,d,x):

    if ((x>a) and (x<b)):
        derajatKeanggotaan = (x-a)/(b-a)

    elif ((x>=b) and (x<=c)):
        derajatKeanggotaan = 1

    elif ((x>c) and (x<d)):
        derajatKeanggotaan = -((x-d)/(d-c))

    else:
        derajatKeanggotaan = 0

    return derajatKeanggotaan

def derajatKesadahan(kesadahan):

    global derajatkesadahanlunak
    global derajatkesadahanmedium
    global derajatkesadahankeras

    derajatkesadahanlunak = fungsiKeanggotaanTrapesium(kesadahanLunakmin,kesadahanLunakmin,45,kesadahanLunakmax,kesadahan)
    derajatkesadahanmedium = fungsiKeanggotaanTrapesium(kesadahanMediummin,50,145,kesadahanMediummax,kesadahan)
    derajatkesadahankeras = fungsiKeanggotaanTrapesium(kesadahanKerasmin,150,kesadahanKerasmax,kesadahanKerasmax,kesadahan)
    
    print("Derajat Kesadahan Lunak   : ",derajatkesadahanlunak)
    print("Derajat Kesadahan Medium  : ",derajatkesadahanmedium)
    print("Derajat Kesadahan Keras   : ",derajatkesadahankeras)

def derajatKekeruhan(kekeruhan):

    global derajatkekeruhanbersih
    global derajatkekeruhancukupbersih
    global derajatkekeruhankeruh

    derajatkekeruhanbersih      = fungsiKeanggotaanTrapesium(kekeruhanBersihmin,kekeruhanBersihmin,5,kekeruhanBersihmax,kekeruhan)
    derajatkekeruhancukupbersih = fungsiKeanggotaanTrapesium(kekeruhanCukupBersihmin,10,20,kekeruhanCukupBersihmax,kekeruhan)
    derajatkekeruhankeruh       = fungsiKeanggotaanTrapesium(kekeruhanKeruhmin,25,kekeruhanKeruhmax,kekeruhanKeruhmax,kekeruhan)
    
    print("Derajat Kekeruhan Bersih       : ",derajatkekeruhanbersih )
    print("Derajat Kekeruhan Cukup Bersih : ",derajatkekeruhancukupbersih)
    print("Derajat Kekeruhan Keruh        : ",derajatkekeruhankeruh)

def derajatTDS(tds):

    global derajattdsbaik
    global derajattdsburuk
    global derajattdssangatburuk

    derajattdsbaik              = fungsiKeanggotaanTrapesium(TDSBaikmin,TDSBaikmin,500,TDSBaikmax,tds)
    derajattdsburuk             = fungsiKeanggotaanTrapesium(TDSBurukmin ,900,1150,TDSBurukmax,tds)
    derajattdssangatburuk       = fungsiKeanggotaanTrapesium(TDSSangatBurukmin,1200,TDSSangatBurukmax,TDSSangatBurukmax,tds)
    
    print("Derajat TDS Baik         : ",derajattdsbaik)
    print("Derajat TDS Buruk        : ",derajattdsburuk)
    print("Derajat TDS Sangat Buruk : ",derajattdssangatburuk)


def main():

    data = []
    n = int(input("Masukkan jumlah data : "))

    for i in range(1, n+1):

        kesadahan = float(input("Masukkan nilai Kesadahan: "))
        kekeruhan = float(input("Masukkan nilai Kekeruhan : "))
        tds = float(input("Masukkan nilai TDS : "))
        t0 = time()

        print("\n==========  PROSES FUZZYFICATION   ==========\n")
        print("\n========== Derajat Keanggotaan Kesadahan ==========\n")
        dKesadahan = derajatKesadahan(kesadahan)

        print("\n========== Derajat Keanggotaan Kekeruhan ==========\n")
        dKekeruhan = derajatKekeruhan(kekeruhan)

        print("\n========== Derajat Keanggotaan TDS ==========\n")
        dTDS = derajatTDS(tds)

        print("\n========== PROSES INTERFERENCES ==========\n")
        fuzzyRules(kesadahan, kekeruhan, tds)

        print("\n========== PROSES DEFUZZYFICATION ==========\n")

        DEFUZZYFICATION = centroidMethod(nilaikelayakanrendah,nilaikelayakantinggi)
        print(DEFUZZYFICATION)
        DEFUZZY = data.append(DEFUZZYFICATION)
        t1 = time() - t0
        print("Waktu Eksekusi Fuzzy = ",t1)

    print(data)
    print("data paling besar adalah : ",max(data))
    return 0

if __name__ == "__main__":
    main()