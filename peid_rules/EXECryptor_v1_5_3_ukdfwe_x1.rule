rule _EXECryptor_v1_5_3_ukdfwe
{
	meta:
		description = "EXECryptor v1_5_3"
	strings:
		$a = {E8240000008B4C240CC70117000100C781B800000000????0031C089411489411880A1C1000000FEC331C064FF30648920CCC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
