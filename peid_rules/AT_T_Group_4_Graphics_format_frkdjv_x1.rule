rule _AT_T_Group_4_Graphics_format_frkdjv
{
	meta:
		description = "AT_T Group 4 Graphics format"
	strings:
		$a = {0100??003A03}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
