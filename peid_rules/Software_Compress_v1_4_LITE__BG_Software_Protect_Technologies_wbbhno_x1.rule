rule _Software_Compress_v1_4_LITE__BG_Software_Protect_Technologies_wbbhno
{
	meta:
		description = "Software Compress v1_4 LITE __ BG Software Protect Technologies"
	strings:
		$a = {E800000000812C24AA1A41005DE800000000832C246E8B855D1A41002904248B042489855D1A4100588B855D1A41008B503C03D08B928000000003D08B4A58898D491A41008B4A5C898D4D1A41008B4A60898D551A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
