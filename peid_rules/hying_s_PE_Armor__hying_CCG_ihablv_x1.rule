rule _hying_s_PE_Armor__hying_CCG_ihablv
{
	meta:
		description = "hying_s PE_Armor __ hying_CCG"
	strings:
		$a = {E8AA0000002D??????00000000000000003D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
