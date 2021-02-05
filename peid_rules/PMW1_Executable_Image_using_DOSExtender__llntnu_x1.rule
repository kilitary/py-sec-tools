rule _PMW1_Executable_Image_using_DOSExtender__llntnu
{
	meta:
		description = "PMW1 Executable Image _using DOSExtender_"
	strings:
		$a = {504D5731}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
