rule _LE_Exe_Executable_Image_yoturr
{
	meta:
		description = "LE_Exe Executable Image"
	strings:
		$a = {4C45}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
