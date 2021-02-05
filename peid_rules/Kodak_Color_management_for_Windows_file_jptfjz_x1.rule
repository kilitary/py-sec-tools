rule _Kodak_Color_management_for_Windows_file_jptfjz
{
	meta:
		description = "Kodak Color management for Windows file"
	strings:
		$a = {????????4B434D53}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
