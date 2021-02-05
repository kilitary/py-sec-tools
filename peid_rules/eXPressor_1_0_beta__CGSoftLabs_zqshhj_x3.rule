rule _eXPressor_1_0_beta__CGSoftLabs_zqshhj
{
	meta:
		description = "eXPressor 1_0 beta __ CGSoftLabs"
	strings:
		$a = {E8530300008BF05656E8980300008BC8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
