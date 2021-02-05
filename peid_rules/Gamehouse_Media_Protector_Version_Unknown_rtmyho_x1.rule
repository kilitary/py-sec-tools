rule _Gamehouse_Media_Protector_Version_Unknown_rtmyho
{
	meta:
		description = "Gamehouse Media Protector Version Unknown"
	strings:
		$a = {68????????6A00FF15????????50FF15??????0000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
