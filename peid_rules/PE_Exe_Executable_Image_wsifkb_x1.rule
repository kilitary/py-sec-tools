rule _PE_Exe_Executable_Image_wsifkb
{
	meta:
		description = "PE_Exe Executable Image"
	strings:
		$a = {50450000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
