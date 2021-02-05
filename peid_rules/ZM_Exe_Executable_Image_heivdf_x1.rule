rule _ZM_Exe_Executable_Image_heivdf
{
	meta:
		description = "ZM_Exe Executable Image"
	strings:
		$a = {5A4D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
