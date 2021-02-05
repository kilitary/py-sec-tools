rule _ASPack_v1_08_04_xbpmby
{
	meta:
		description = "ASPack v1_08_04"
	strings:
		$a = {60E8????????EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
