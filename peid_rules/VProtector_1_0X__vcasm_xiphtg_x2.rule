rule _VProtector_1_0X__vcasm_xiphtg
{
	meta:
		description = "VProtector 1_0X __ vcasm"
	strings:
		$a = {00005669727475616C416C6C6F630000000000766361736D5F70726F746563745F????????????????????0000000000000000000000000000000000000000000000000033F6E8100000008B642408648F05000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
