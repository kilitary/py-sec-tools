rule _Microsoft_Windows_Metafile_zspxdy
{
	meta:
		description = "Microsoft Windows Metafile"
	strings:
		$a = {D7CDC69A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
