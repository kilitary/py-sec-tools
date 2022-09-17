rule _EXECryptor_v1_4_0_1_snrqbd
{
	meta:
		description = "EXECryptor v1_4_0_1"
	strings:
		$a = {E8240000008B4C240CC70117000100C781B800000000????0031C089411489411880}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
