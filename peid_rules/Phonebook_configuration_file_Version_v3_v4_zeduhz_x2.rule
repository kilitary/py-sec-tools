rule _Phonebook_configuration_file_Version_v3_v4_zeduhz
{
	meta:
		description = "Phonebook configuration file Version _v3__v4"
	strings:
		$a = {50686F6E65626F6F6B??????????????????????????636F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
