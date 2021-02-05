rule _Symantec_WinFax_PRO_8_3_Coverpage_ghbrfc
{
	meta:
		description = "Symantec WinFax PRO 8_3 Coverpage"
	strings:
		$a = {FFFF??????????436F7665724461746162617365}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
