rule _kkrunchy_0_23_alpha_2__Ryd_jykvex
{
	meta:
		description = "kkrunchy 0_23 alpha 2 __ Ryd"
	strings:
		$a = {BD????????C74500??????00B8??????0089450489455450C74510??????00FF4D0CFF4514FF4558C6451C08B8000800008D7D30ABABABABBB0000D800BF??????0131C9418D740901B8CA8E2A2E99F7F601C389D8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
