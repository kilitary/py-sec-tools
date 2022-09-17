rule _ASYLUM_Music_File_v_1_0_ojhghp
{
	meta:
		description = "ASYLUM Music File v_1_0"
	strings:
		$a = {4153594C554D204D7573696320466F726D61742056312E3000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
