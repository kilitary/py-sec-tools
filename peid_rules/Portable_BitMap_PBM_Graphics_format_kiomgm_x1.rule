rule _Portable_BitMap_PBM_Graphics_format_kiomgm
{
	meta:
		description = "Portable BitMap _PBM_ Graphics format"
	strings:
		$a = {50360A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
