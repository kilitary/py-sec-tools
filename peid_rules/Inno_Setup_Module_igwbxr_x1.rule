rule _Inno_Setup_Module_igwbxr
{
	meta:
		description = "Inno Setup Module"
	strings:
		$a = {496E6E6F53657475704C647257696E646F770000535441544943}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
