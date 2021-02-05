rule _Microsoft_Visual_C__DLL_ycpxhn
{
	meta:
		description = "Microsoft Visual C__ DLL"
	strings:
		$a = {53B8010000008B5C240C565785DB557512833D??????????750933C0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
