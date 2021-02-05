rule _MS_Compress_Archive_vsdlqw
{
	meta:
		description = "MS Compress Archive"
	strings:
		$a = {535A4444}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
