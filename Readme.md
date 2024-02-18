## Jak rozbít RSA když vygenerujeme prvočísla p a q moc blízko k sobě?

Vašim cílem je dešifrovat tuto zprávu (enkódováno v hex):

***7da8ffed704d231c7d8e26a61bf2da342b7e22bf1652f032588b301fb05ace8194ac1a6e82958bfd27fc653de572d6418ab8e92ff2ff82f89ca036fdad87ab5846c9c58d43e1659764db80f9057b3f6bb51faf9e96fd87dfb60a5d74e54b4f0049fd920d013d034e3677ed8f2ecd06be22825db4d395e1418b4fa9f490dd60f3***
Která byla zašifrována tímto veřejným klíčem:

```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCIDHP5EkMPaQ3FDL9yoHMREia5
WiTin3D2rwFvcCDc+AuVm0HiywEQQF8ZxOO4hEfvmXzVqPSojkkarDNqe8hQvsGx
lv/EjvL6ULf60Yt5BrlbLKnpkhcYSj0YRBf24lzQD8D2vzNlaW16aJXbwUzdaHN/
jUczApfsrMtkeVrirwIDAQAB
-----END PUBLIC KEY-----
```
Bylo použito šifrovací schéma PKCS#1 OAEP. Vlajka je ve formátu: haxagon{...}.

*PS: Doporučuji Python.*