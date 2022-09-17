rule _EXECryptor_v1_3_0_45_gpmncm
{
	meta:
		description = "EXECryptor v1_3_0_45"
	strings:
		$a = {E824??????8B4C240CC70117??01??C781??????????????31C089411489411880A1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
