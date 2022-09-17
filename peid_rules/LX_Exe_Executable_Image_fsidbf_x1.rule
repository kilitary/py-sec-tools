rule _LX_Exe_Executable_Image_fsidbf
{
	meta:
		description = "LX_Exe Executable Image"
	strings:
		$a = {4C58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
