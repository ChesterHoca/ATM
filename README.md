atm adı altında dictionary oluşturdum ve 3 ID'li kullanıcı oluşturdum.

while döngüsüne true verdim.

user ve selection adlı 2 değişken oluşturdum.

ilk başta if ile selectiona {(atm[user]['Main']) + (atm[user]['Sub'])} içeriği atadım. Bu sayede kullanıcı güncel main ve sub bakiyesinin toplamını görebiliyor. Ayrıca break ile çalıştırmayı durdurdum.

money_out adlı değişken oluşturdum ve kullanıcıya çekecek bakiyesini sordum.

if ile sol taraftaki verinin sağ tarafta yer alan veri ile eşit olup olmadığını sorgulattım.

eğer bakiye var ise kullanıcıdan "Main" yani ana parasını money_out'a girilen miktar kadar eksilmesini söyledim.

quest değişkeni oluşturdum ve hesapta bakiye bulunmuyorsa "Sub" yani diğer hesaptan çekelim mi diye sordum y/n.

eğer y denilirse atm[user]['Main'] += atm[user]['Sub'] ile topladım ve money_out ile çıkışını yaptım.

else ile eğer bakiye orada da yoksa print ile yetersiz bakiye yazısını yazdırdım.

eğer kullanıcı n seçerse gerçekleştirilmedi hatası ile karşılaşacaktır.

son olarak else ile ise y/n yazılmazsa seçim yanlışı yaptırmayı söyledim.

selection == 4: ile ise direkt çıkış yapılıyor.

kodun son kısmında ise yanlış seçim yapılırsa çıkış yapacak ve break ile sonlandırılacaktır.
