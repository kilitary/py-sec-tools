rule _ExeShield_Protector_V3_6__www_exeshield_com_sipuin
{
	meta:
		description = "ExeShield Protector V3_6 __ www_exeshield_com"
	strings:
		$a = {2C711BCAEB012AEB01658D3580????0080C98480C968BBF4000000EB01EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
