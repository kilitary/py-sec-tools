rule _XE_Executable_Image_using_DOSExtender__gjjhqx
{
	meta:
		description = "XE Executable Image _using DOSExtender_"
	strings:
		$a = {5845}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
