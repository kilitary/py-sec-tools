rule _PEncrypt_v3_1_lnmbbj
{
	meta:
		description = "PEncrypt v3_1"
	strings:
		$a = {E9????509CFCBE????8BFE8CC805????8EC00657B9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
