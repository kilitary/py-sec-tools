rule _APatch_GUI_v1_1_vlogjd
{
	meta:
		description = "APatch GUI v1_1"
	strings:
		$a = {5231C0E8FFFFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
