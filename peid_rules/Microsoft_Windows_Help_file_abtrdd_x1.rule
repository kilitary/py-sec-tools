rule _Microsoft_Windows_Help_file_abtrdd
{
	meta:
		description = "Microsoft Windows Help file"
	strings:
		$a = {3F5F03}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
