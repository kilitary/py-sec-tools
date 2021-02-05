rule _UnoPiX_1_03_1_10__BaGiE_uvhcor
{
	meta:
		description = "UnoPiX 1_03_1_10 __ BaGiE"
	strings:
		$a = {83EC04C7042400??????C300????00000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
