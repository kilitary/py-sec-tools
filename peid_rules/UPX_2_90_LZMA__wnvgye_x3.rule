rule _UPX_2_90_LZMA__wnvgye
{
	meta:
		description = "UPX 2_90 _LZMA_"
	strings:
		$a = {60BE????????8DBE????????5783CDFFEB109090909090908A064688074701DB75078B1E83EEFC11DB72EDB80100000001DB75078B1E83EEFC11DB11C001DB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
