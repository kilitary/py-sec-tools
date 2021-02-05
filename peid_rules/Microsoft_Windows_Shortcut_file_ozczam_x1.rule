rule _Microsoft_Windows_Shortcut_file_ozczam
{
	meta:
		description = "Microsoft Windows Shortcut file"
	strings:
		$a = {4C000000011402000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
