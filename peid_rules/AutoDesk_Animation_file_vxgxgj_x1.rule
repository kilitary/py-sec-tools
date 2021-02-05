rule _AutoDesk_Animation_file_vxgxgj
{
	meta:
		description = "AutoDesk Animation file"
	strings:
		$a = {??????0012AF????4001C8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
