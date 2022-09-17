rule _RCryptor_v1_1__Vaska_usorcb
{
	meta:
		description = "RCryptor v1_1 __ Vaska"
	strings:
		$a = {90589050908B00903C5090580F8567D6EF11506800101413B8001014133D0064141374068030BC40EBF3E800000000C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
