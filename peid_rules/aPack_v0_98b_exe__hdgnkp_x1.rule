rule _aPack_v0_98b_exe__hdgnkp
{
	meta:
		description = "aPack v0_98b _exe_"
	strings:
		$a = {93071F05????8ED0BC????EA}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
