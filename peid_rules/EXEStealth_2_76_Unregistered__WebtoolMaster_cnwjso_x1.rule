rule _EXEStealth_2_76_Unregistered__WebtoolMaster_cnwjso
{
	meta:
		description = "EXEStealth 2_76 Unregistered __ WebtoolMaster"
	strings:
		$a = {EB??457865537465616C74682056322053686172657761726520}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
