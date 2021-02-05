rule _NE_Exe_Executable_Image_dcluef
{
	meta:
		description = "NE_Exe Executable Image"
	strings:
		$a = {4E45}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
