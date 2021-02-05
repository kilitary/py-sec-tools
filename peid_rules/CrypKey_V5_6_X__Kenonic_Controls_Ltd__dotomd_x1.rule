rule _CrypKey_V5_6_X__Kenonic_Controls_Ltd__dotomd
{
	meta:
		description = "CrypKey V5_6_X __ Kenonic Controls Ltd_"
	strings:
		$a = {E8????????E8????????83F80075076A00E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
