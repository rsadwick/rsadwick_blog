module.exports = function (grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            css: {
            src: [
                 'css/*'
                ],
            dest: 'css/ryan.all.css'
            },
            js : {
                src : [
                    'js/libs/jquery.js',
                    'js/libs/foundation.js',
                    'js/libs/slick/slick.js',
                    'js/app.js'
                ],
                dest : 'js/ryan.all.js'
            }
        },
        cssmin: {
            css: {
                src: 'css/ryan.all.css',
                dest: 'css/ryan.min.css'
            }
        },
        uglify: {
            js: {
              files: {
                'js/ryan.min.js': ['js/ryan.all.js']
              }
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.registerTask('default', [ 'concat:css', 'cssmin:css', 'concat:js', 'uglify:js' ]);

};