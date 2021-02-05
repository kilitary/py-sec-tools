rule _ExeBundle_v3_0_small_loader__palisa
{
	meta:
		description = "ExeBundle v3_0 _small loader_"
	strings:
		$a = {0000000060BE00F040008DBE0020FFFF5783CDFFEB109090909090908A064688074701DB75078B1E83EEFC11DB72EDB80100000001DB75078B1E83EEFC11}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
