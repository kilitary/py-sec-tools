rule _WIBU_Key_V4_10A__http_wibu_comus_nnojjk
{
	meta:
		description = "WIBU_Key V4_10A __ http_wibu_comus"
	strings:
		$a = {F705????????FF0000007512}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
