rule _WARNING__TROJAN__XiaoHui_egiarp
{
	meta:
		description = "WARNING __ TROJAN __ XiaoHui"
	strings:
		$a = {609CE8000000005DB8??8540002D??854000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
