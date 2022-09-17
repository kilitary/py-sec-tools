rule _Vterminal_V1_0X__Lei_Peng_yptcab
{
	meta:
		description = "Vterminal V1_0X __ Lei Peng"
	strings:
		$a = {E8000000005805????????9C50C20400}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
