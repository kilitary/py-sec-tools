rule _CAN2EXE_v0_01_dzediq
{
	meta:
		description = "CAN2EXE v0_01"
	strings:
		$a = {268E06????B9????33C08BF8F2AEE3??26380575??EB??E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
