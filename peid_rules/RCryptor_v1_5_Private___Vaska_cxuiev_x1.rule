rule _RCryptor_v1_5_Private___Vaska_cxuiev
{
	meta:
		description = "RCryptor v1_5 _Private_ ___ Vaska"
	strings:
		$a = {832C244F68????????FF542404834424044FB8????????3D????????74068030??40EBF3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
