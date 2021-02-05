rule _Free_Pascal_v1_0_10_win32_GUI__ergrgn
{
	meta:
		description = "Free Pascal v1_0_10 _win32 GUI_"
	strings:
		$a = {C605??????0000E8????000050E800000000FF25??????005589E5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
