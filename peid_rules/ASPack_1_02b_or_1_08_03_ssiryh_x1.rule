rule _ASPack_1_02b_or_1_08_03_ssiryh
{
	meta:
		description = "ASPack 1_02b or 1_08_03"
	strings:
		$a = {60E8000000005D81ED}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
